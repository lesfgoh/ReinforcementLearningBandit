Overview:

This project is a web-based application that simulates a Multi-Armed Bandit problem, as presented in course MH4521 from SPMS, NTU.
It allows users to interact with different bandit arms, each associated with a specific probability distribution. 
Users can configure the type of distributions for each arm, customize their parameters, and visualize the rewards generated from pulling the arms.

Features:

	•	Customizable Bandits: Choose the type of distribution (Normal, Uniform, Beta, Bernoulli) for each arm and set their parameters.
	•	Interactive UI: Pull different arms to observe the rewards generated from various distributions.
	•	Reward Visualization: View a chart that displays the distribution of rewards for each arm.
	•	Reset Functionality: Start over by resetting the current state of the bandit.

Stack:

	•	Flask: Backend web framework.
	•	HTML/CSS/JavaScript: Frontend to create a responsive and interactive user interface.
	•	NumPy: Numerical computations, especially for generating random numbers based on distributions.

 
For Installation:

Please clone this project via `https://github.com/lesfgoh/ReinforcementLearningBandit.git`.

Create a virtual environmet: 
```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
`pip install -r requirements.txt`
 
Run the web app:
`python bandit.py`

Finally, to access the web app, please go to `http://127.0.0.1:5000/` on your web browser.
