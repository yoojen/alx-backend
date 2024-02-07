import createPushNotificationsJobs from './8-job';
import { createQueue } from 'kue';
import chai from 'chai';
import sinon from 'sinon';

const Queue = createQueue();
const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153638785',
    message: 'This is the code 4567 to verify your account',
  },
];

describe('createPushNotificationsJobs', () => {
  beforeEach(() => {
    sinon.spy(console, 'log');
  });

  before(() => {
    Queue.testMode.enter();
  });

  afterEach(() => {
    sinon.restore();
    Queue.testMode.clear();
  });

  after(() => {
    Queue.testMode.exit();
  });

  it('error message if jobs is not instance of array', () => {
    expect(() => createPushNotificationsJobs(5, Queue)).to.throw();
    expect(() => createPushNotificationsJobs(5, Queue)).to.throw(
      /Jobs is not an array/
    );
  });

  it('throws error if queue is not a valid kue', function () {
    expect(() => createPushNotificationsJobs(jobs, '')).to.throw();
  });

  it('create two new jobs to the queue ', () => {
    createPushNotificationsJobs(jobs, Queue);
    expect(Queue.testMode.jobs.length).to.equal(2);
    expect(Queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(Queue.testMode.jobs[0].data).to.eql(jobs[0]);
    expect(
      console.log.calledOnceWith(
        `Notification job created: ${Queue.testMode.jobs[0].id}`
      )
    ).to.be.true;
  });
});
