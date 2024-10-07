# Prompt

What does RPO and RTO mean in backup terms. If I want to take backups often enough that I would suffer minimal data loss between now and the rollback, which variable am I trying to minimise? 
# Output

In backup terms:

- **RPO (Recovery Point Objective)** refers to the maximum acceptable amount of data loss measured in time. It indicates how far back in time your backup or recovery system can go to restore the system to a previous state. For instance, if your RPO is 4 hours, your system must back up data often enough that, in case of failure, you lose no more than 4 hours' worth of data.
  
- **RTO (Recovery Time Objective)** is the maximum acceptable time your system can be offline before it must be fully restored. It focuses on how quickly you can recover from an outage or failure.

If you want to **minimize data loss**, you're aiming to **minimize RPO** by taking backups more frequently, so the data between the last backup and the failure is as minimal as possible. 

In this case, you're focusing on **RPO**.