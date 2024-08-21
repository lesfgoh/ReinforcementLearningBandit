import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, redirect, url_for
import numpy as np

app = Flask(__name__)


class MultiArmedBandit:
    
    def __init__(self, arms, distribution):
        self.arms = arms
        self.dist = distribution
        self.params= [self.generate_params(dist) for dist in distribution]
        self.results = [[] for _ in range(5)]
    

    def generate_params(self, dist):
        if dist in ["normal", "uniform", "beta"]:
            return (np.random.uniform(0,10), np.random.uniform(0,10))
        else:
            return np.random.randint
        
    def generate_reward(self, arm):
        dist = self.dist[arm]
        param = self.params[arm]
        match dist:
            case "normal":
                self.results[arm] += [[np.random.normal(*param)]]
            case "beta":
                self.results[arm] += [np.random.beta(*param)]
            case "uniform":
                self.results[arm] += [np.random.uniform(*param)]
            case _:
                print("There is an issue here. No cases match the dist.")

    def reset(self):
        self.params = [self.generate_params(dist) for dist in self.dist]
        self.results = [[] for _ in range(5)]


# params = [(1, 1), (2, 1), (2, 5), (0, 1), 0.7]



@app.route('/')
def index():
    return render_template('index.html', arms=range(bandit.arms), params=bandit.params, rewards = bandit.results, dist = bandit.dist)

@app.route('/pull/<int:arm>', methods=['GET'])
def pull(arm):
    reward = bandit.generate_reward(arm)
    return render_template('result.html', arm=arm, reward=bandit.results[arm], param=bandit.params[arm], dist = bandit.dist[arm])

@app.route('/reset')
def reset():
    bandit.reset()
    return redirect(url_for('index'))

@app.route('/entry', methods=['GET', 'POST'])
def entry():
    if request.method == 'POST':
        n_arms = int(request.form['n_arms'])
        distributions = [request.form[f'dist_{i}'] for i in range(n_arms)]

        global bandit
        bandit = MultiArmedBandit(n_arms, distributions)
        return redirect(url_for('index'))

    return render_template('entry.html')


if __name__ == '__main__':
    app.run(debug=True)