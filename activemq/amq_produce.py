import stomp

location_queue = "test-activemq-queue"
conn = stomp.Connection([('143.198.60.1', 61613)])
conn.connect(username='admin', passcode='admin', wait=True)


def send_to_queue(msg):
    conn.send(body=str(msg), destination=location_queue)
    print(msg)


if __name__ == '__main__':
    send_to_queue('len 123')
    conn.disconnect()
