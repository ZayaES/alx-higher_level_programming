#include <stdlib.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *behind, *ahead;


	if (list == NULL || list->next == NULL)
		return (0);

	behind = list->next;
	ahead = list->next->next;

	while (behind && ahead && ahead->next)
	{
		if (behind == ahead)
			return (1);

		behind = behind->next;
		ahead =ahead->next->next;
	}

	return (0);
}
