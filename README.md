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

Create a virtual environment: 
```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
`pip install -r requirements.txt`
 
Run the web app via terminal:
`python bandit.py`

Finally, to access the web app, please go to `http://127.0.0.1:5000/entry` on your web browser.

It should look like the following:

<img width="483" alt="Screenshot 2024-08-21 at 6 05 21 PM" src="https://github.com/user-attachments/assets/dc3c6f99-d2cf-413d-ba88-f840a6b16da8">
<img width="1462" alt="Screenshot 2024-08-21 at 6 09 24 PM" src="https://github.com/user-attachments/assets/f7e5fc6c-2e2d-4b06-a04b-40d636493515">
<img width="449" alt="Screenshot 2024-08-21 at 6 06 32 PM" src="https://github.com/user-attachments/assets/31e7feba-9fab-4886-879a-65d7e8c71eae">





[Multi-Armed Bandit Game.pdf](https://github.com/user-attachments/files/16690000/Multi-Armed.Bandit.Game.pdf)

