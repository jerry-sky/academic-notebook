with Node; use Node;

package Sender is

    task type SenderTask(firstNode: pNodeObj; k: Natural; h: Natural);

    type pSenderTask is access SenderTask;

end Sender;
