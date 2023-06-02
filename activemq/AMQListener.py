import stomp
import datetime
import time
import sched

enableGetTask = True

class AMQListener(object):

    def __init__(self):
        self.location_queue = "test-activemq-queue"
        self.conn = stomp.Connection([('188.166.120.249', 61613)])

    def on_message(self, message):
        global enableGetTask
        enableGetTask = False
        print('message: %s' % message.body)
        time.sleep(10)
        enableGetTask = True

    def receive_from_queue(self):
        if enableGetTask:
            print("Server is free and re-connect")
            self.conn.connect(username='admin', passcode='admin', wait=True)
            self.conn.set_listener('SampleListener', AMQListener())
            self.conn.subscribe(self.location_queue, 12)
            self.conn.disconnect()
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
