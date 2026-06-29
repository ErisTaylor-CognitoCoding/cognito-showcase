from Reset import reset
from Main import main
from pumpkins import pumpkins
from Sunflowers import sunflowers

def controller():
	last_crop = None
	while True:
		Power = num_items(Items.Power)
		if last_crop == "sunflowers":
			if Power> 20000:
				reset()
				last_crop = "main"
				main()
			else:
				sunflowers()
		else:
			if Power < 5000:
				reset()
				last_crop = "sunflowers"
				sunflowers()
			else:	
				Carrots = num_items(Items.Carrot)
				if last_crop == "main":
					if Carrots > 5000:
						reset()
						last_crop = "pumpkins"
						pumpkins()
					else:
						main()
				else:
					if Carrots < 1000:
						reset()
						last_crop = "main"
						main()
					else:
						if last_crop != "pumpkins":
							reset()
							last_crop = "pumpkins"
						pumpkins()
		
controller()
