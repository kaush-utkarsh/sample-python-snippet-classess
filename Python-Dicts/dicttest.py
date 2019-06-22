#http://collabedit.com/3ubwm

dicty = {
	"q1": {
		"text": "question 1 text",
		"options":
		{
			"1":{
				"text":"optext1",
				"jump":"q2"
			},
			"2":{
				"text":"optext2",
				"jump":"q1"
			},
			"3":{
				"text":"optext1",
				"jump":-1
			}
		}
	},
	"q2": {
		"text": "question 2 text",
		"options":
		{
			"1":{
				"text":"optext1",
				"jump":"q2"
				},
			"2":{
				"text":"optext2",
				"jump":"q1"
				},
			"3":{
				"text":"optext1",
				"jump":-1
			}
		}
	}
}


print (dicty["q1"]["options"]["3"]["jump"])