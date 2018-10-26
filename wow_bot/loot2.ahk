;~R::

while true
{
	sleep, 1000
	Attack()
	Loot()
	;Turn(35, "right")
	;Arrange_cam("right")
	;Attack()
	;Loot()
	;Turn(35, "left")
	;Arrange_cam("left")
	send, {F1}
}


Arrange_cam(side)
{
	if (side == "right")
	{
		send, {RButton Down}
		MouseMove, -1, 1, 1, R
		send, {RButton Up}
	} else {
		send, {RButton Down}
		MouseMove, 1, -1, 1, R
		send, {RButton Up}
	}
}


Turn(deg, side)
{	
	if (side = "right")
	{
		sleep_time := (1978*deg)/(360) 
		send, {right Down}
		sleep, sleep_time
		send, {right Up}
	} else {
		sleep_time := (1978*deg)/(360) 
		send, {left Down}
		sleep, sleep_time
		send, {left Up}
	}
}

Walk(yard, side)
{
	if (side == "fwd")
	{
		sleep_time := (15.5*yard)/(100) * 1000
		send, {W Down}
		sleep, sleep_time
		send, {W Up}
	} else {
		sleep_time := (15.5*yard)/(100) * 1000
		send, {S Down}
		sleep, sleep_time
		send, {S Up}
	}
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
	x := 820
	y := 550
	MouseMove, x, y

	Loop, 4
	{
		Loop, 2
		{
			send, {Shift Down} {RButton}
			send, {Shift Up}
			sleep, 600
			send, {Shift Down} {RButton}
			send, {Shift Up}
			sleep, 600
		}
		x := x - 60
		y := y - 60
		MouseMove, x, y

	}

	x := 570
	y := 550
	MouseMove, x, y

	Loop, 4
	{
		Loop, 2
		{	
			send, {Shift Down} {RButton}
			send, {Shift Up}
			sleep, 600
			send, {Shift Down} {RButton}
			send, {Shift Up}
			sleep, 600
		}
		x := x + 60
		y := y - 60
		MouseMove, x, y
	}

}

;Turns 180 degree per 1980 microsecond
;Runs 100 yards pers 15.5 secs

Escape::ExitApp
