with External; use External;

package Receiver is

    task type ReceiverTask(k: Natural) is
        entry ReceiveMessage;
        entry Ended;
    end ReceiverTask;

    type pReceiverTask is access ReceiverTask;

end Receiver;
