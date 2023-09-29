#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - Runs an infinite loop with a delay
 *
 * This function enters an infinite loop with a 1-second
 * sleep delay in each iteration.
 * It is used to keep the program running indefinitely.
 *
 * Return: 0 on completion (never reached)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * create_zombies - Create zombie processes
 *
 * This function forks child processes to create zombie processes.
 *
 * Return: 0 on success, 1 on failure
 */
int create_zombies(void)
{
	pid_t child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();

		if (child_pid == -1)
		{
			perror("fork");
			return (1);
		}

		if (child_pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}

	return (0);
}


/**
 * main - Entry point of the program
 *
 *	This function creates 5 zombie processes
 *	using the create_zombie function
 *	and then enters an infinite loop to keep the program running.
 *
 * Return: Always 0
 */

int main(void)
{
	if (create_zombies() != 0)
	{
		return (1);
	}

	infinite_while();

	return (0);
}
