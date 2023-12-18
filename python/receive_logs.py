import logging
import logging.handlers
import socketserver


class LogRecordStreamHandler(socketserver.StreamRequestHandler):
    def handle(self):
        while True:
            try:
                record = self.request.recv(4096)
                if not record:
                    break
                record = logging.makeLogRecord(record)
                self.handle_log_record(record)
            except Exception as e:
                logging.error(e)
                break

    def handle_log_record(self, record):
        logger = logging.getLogger(record.name)
        logger.handle(record)


if __name__ == "__main__":
    server = socketserver.TCPServer(("localhost", 9000), LogRecordStreamHandler)
    server.serve_forever()
