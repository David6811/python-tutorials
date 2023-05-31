import stomp
import datetime
import time
import sched


class AMQListener(object):

    def __init__(self):
        self.location_queue = "test-activemq-queue"
        self.conn = stomp.Connection([('127.0.0.1', 61613)])
        self.conn.connect(username='admin', passcode='admin', wait=True)

    def on_message(self, message):
        print('message: %s' % message.body)

    def receive_from_queue(self):
        self.conn.set_listener('SampleListener', AMQListener())
        self.conn.subscribe(self.location_queue, 12)
        # while True:
        #     pass

    def time_task(self):
        now = datetime.datetime.now()
        ts = now.strftime('%Y-%m-%d %H:%M:%S')
        print('do func time :', ts)
        self.receive_from_queue()
        self.loop_monitor()

    def loop_monitor(self):
        s = sched.scheduler(time.time, time.sleep)
        s.enter(5, 1, self.time_task, ())
        s.run()


if __name__ == '__main__':
    sampleListener = AMQListener()
    sampleListener.receive_from_queue()
