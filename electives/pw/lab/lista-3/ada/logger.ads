with External; use External;

package Logger is

    task type LoggerReceiver is
        entry Log(message: String);
        entry Stop;
    end LoggerReceiver;

    type pLoggerReceiver is access LoggerReceiver;

end Logger;
