import express from 'express';
import { promisify } from 'util';
import { createClient } from 'redis';

const client = createClient();

client.on('err', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

const listProducts = [
  { Id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { Id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { Id: 3, name: ' Suitcase 650', price: 350, stock: 2 },
  { Id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

function listNewShape(product) {
  const newShape = {};
  newShape.itemId = product.Id;
  newShape.itemName = product.name;
  newShape.price = product.price;
  newShape.initialAvailableQuantity = product.stock;
  return newShape;
}

function allItems() {
  return listProducts.map(listNewShape);
}
function getItemById(id) {
  listProducts.map((product) => {
    if (product.Id === id) {
      return listNewShape(product);
    }
  });
  return {};
}

function reserveStockById(itemId, stock) {
  const SET = promisify(client.SET).bind(client);
  return SET(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const GET = promisify(client.GET).bind(client);
  stock = await reserveStockById(`item.${itemId}`);
  if (stock === null) return 0;
  return stock;
}
const app = express();

app.get('/list_products', (req, res) => {
  return res.json(allItems());
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const product = getItemById(itemId);
  if (Object.values(product).length > 0) {
    const stock = await getCurrentReservedStockById(itemId);
    product.currentQuantity = product.initialAvailableQuantity - stock;
    return res.json(product);
  }
  return res.json({ status: 'Product not found' });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = Number(req.params.itemId);
  const product = getItemById(itemId);
  if (Object.values(product).length === 0) {
    return res.json({ status: 'Product not found' });
  }
  const stock = await getCurrentReservedStockById(itemId);
  if (stock >= product.initialAvailableQuantity) {
    return res.json({ status: 'Not enough stock available', itemId });
  }
  await reserveStockById(itemId, Number(stock) + 1);
  return res.json({ status: 'Reservation confirmed', itemId });
});

function clearRedisStock() {
  const SET = promisify(redisClient.SET).bind(redisClient);
  return Promise.all(listProducts.map((item) => SET(`item.${item.Id}`, 0)));
}
app.listen(1245, async () => {
  await clearRedisStock();
  console.log('API available on localhost via port 1245');
});
