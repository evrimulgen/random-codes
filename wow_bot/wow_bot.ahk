;~R::

while true
{	
	Attack()
	Loot()
	Turn(90, "right")
	send, {F1}
}
Turn(deg, side)
{	
	if (side = "right")
	{
		sleep_time := (1980*deg)/(180) 
		send, {right Down}
		sleep, sleep_time
		send, {right Up}
	} else {
		sleep_time := (1980*deg)/(180) 
		send, {left Down}
		sleep, sleep_time
		send, {left Up}
	}
}

Walk(yard)
{
	sleep_time := (15.5*yard)/(100) * 1000
	send, {W Down}
	sleep, sleep_time
	send, {W Up}
}

Attack()
{
	send, {Tab}
	sleep, 1000
	send, {G}
	sleep, 1000

	Loop, 5
	{
		Loop, 5
		{
			send, {1}
			sleep, 2000
		}
		send, {3}
	}
}

Loot()
{
	x := 680
	y := 385
	MouseMove, x, y

	Loop, 4
	{
		Loop, 2
		{
			send, {Shift Down} {RButton}
			sleep, 1000
			send, {Shift Up}
			sleep, 1000
		}
		x := x - 9
		y := y - 9
		MouseMove, x, y

	}

	x := 689
	y := 394
	MouseMove, x, y

	Loop, 4
	{
		Loop, 2
		{	
			send, {Shift Down} {RButton}
			sleep, 1000
			send, {Shift Up}
			sleep, 1000
		}
		x := x + 9
		y := y + 9
		MouseMove, x, y
	}

}

;Turns 180 degree per 1980 microsecond
;Runs 100 yards pers 15.5 secs

Escape::ExitApp
