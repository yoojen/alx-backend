import { createQueue } from 'kue';

const blacklisted = ['4153518780', '4153518781'];
const Queue = createQueue();

function sendNotification(phoneNumber, message, job, done) {
  let progress = job.data.progress;
  const total = 100;
  if (blacklisted.includes(job.data.phoneNumber)) {
    return done(
      new Error(`Phone number ${job.data.phoneNumber} is blacklisted`)
    );
  }
  if (progress === 0 || p == total / 2) {
    console.log(
      `Sending notification to ${phoneNumber}, with message: ${message}`
    );
  }
}

Queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
