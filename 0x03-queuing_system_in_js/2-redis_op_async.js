import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();
client
  .on('error', (err) => {
    console.log('Redis client not connected to the server:', err.toString());
  })
  .on('connect', () => {
    console.log('Redis client connected to the server');
  });

function setNewSchool(schoolName, value) {
  client.SET(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  const GET = promisify(client.GET).bind(client);
  try {
    const res = await GET(schoolName);
    console.log(res);
  } catch (error) {
    console.log(error);
  }
}

(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
