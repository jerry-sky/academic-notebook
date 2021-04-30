
package body Receiver is

    task body ReceiverTask is
        receivedMessagesCount: Natural := 0;
    begin
        loop
            accept ReceiveMessage do
                receivedMessagesCount := Natural'Succ(receivedMessagesCount);
            end ReceiveMessage;
            if k = receivedMessagesCount then
                exit;
            end if;
        end loop;
        accept Ended do
            null;
        end Ended;
    end ReceiverTask;

end Receiver;
