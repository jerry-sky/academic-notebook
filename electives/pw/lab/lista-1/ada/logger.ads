with External;
use External;

package Logger is

    task type LoggerReceiver(n: Natural; d: Natural; k: Natural) is
        entry Log(message: String);
        entry LogMessageInTransit(msg: Natural; node: Natural);
        entry Stop;
    end LoggerReceiver;

    type pLoggerReceiver is access LoggerReceiver;

end Logger;
