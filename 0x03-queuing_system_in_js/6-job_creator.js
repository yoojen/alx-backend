import { createQueue } from 'kue';

const jobObject = {
  phoneNumber: '+250786803121',
  message: 'Kindly share me opportunities',
};
const Queue = createQueue();

const job = Queue.createJob('push_notification_code', jobObject).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
});
job.on('failed', () => {
  console.log('Notification job failed');
});
