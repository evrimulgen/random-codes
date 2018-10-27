#include <stdio.h>

int
main ()
{
  int day, month, year = 0;

  // take input 

printf ("Enter date [year month day]: ");
scanf ("%d %d %d", &year, &month, &day);

  // input validation

  if (year < 0 || day <= 0 || month <= 0)
    {
      printf ("Invalid date.\r\n");
      return 0;
    }

  if (day > 31 || month > 12)
    {
      printf ("Invalid date.\r\n");
      return 0;
    }

  if ((month == 2) && (day > 28))
    {
      printf ("Invalid date.\r\n");
      return 0;
    }

  if ((day > 30) && (month == 4 || month == 6 || month == 9 || month == 11))
    {
      printf ("Invalid date.\r\n");
      return 0;
    }

  // take second input

  int end_year = 0;

  printf ("Enter end year: ");
  scanf ("%d", &end_year);

  if (year > end_year)
    {
      printf ("Invalid year.\n");
    }

  //zeller's conqurence

  if (month == 1)
    {
      month = 13;
      year--;
    }
  if (month == 2)
    {
      month = 14;
      year--;
    }

  int century = year / 100;
  int yearc = year % 100;

  int zeller = day + 13 * (month + 1) / 5 + (5 * yearc) / 4 + (21 * century) / 4;
  int day_number = zeller % 7;

  switch (day_number)
    {
    case 0:
      printf ("It's a Saturday.\r\n");
      break;
    case 1:
      printf ("It's a Sunday.\r\n");
      break;
    case 2:
      printf ("It's a Monday.\r\n");
      break;
    case 3:
      printf ("It's a Tuesday.\r\n");
      break;
    case 4:
      printf ("It's a Thursday.\r\n");
      break;
    case 5:
      printf ("It's a Wednesday.\r\n");
      break;
    case 6:
      printf ("It's a Friday.\r\n");
      break;
    }

    int interval = end_year - year;
    int yearcount = year + 1;
    int coincidence = 0, i = 0;
    
    while(i < interval)
    {
        
    int century2 = yearcount / 100;
    int yearc2 = yearcount % 100;
    
    int zeller2 = day + 13 * (month + 1) / 5 + (5 * yearc2) / 4 + (21 * century2) / 4;
    int day_number2 = zeller2 % 7;
        
    yearcount = yearcount + 1;
        
    if(day_number2 == day_number)
    {
       coincidence++; 
    }
    
    i++;
    
    }
  
    printf ("Same day-and-month on same weekday between %d and %d: %d \n", year, end_year, coincidence);
    
    return 0;
}
