
package body Sender is

    task body SenderTask is
        tmpMessage: pMessage;
        subtype RangeK is Natural range 1..k;
    begin
        for I in RangeK'Range loop
            tmpMessage := new Message'(content => I, health => h);
            firstNode.all.nodeTask.all.SendMessage(tmpMessage);
        end loop;
    end SenderTask;

end Sender;
