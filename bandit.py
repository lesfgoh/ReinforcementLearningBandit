import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import base64
import io
import statistics

app = Flask(__name__)


class MultiArmedBandit:
    
    def __init__(self, arms, distribution):
        self.arms = arms
        self.dist = distribution
        self.params= [self.generate_params(dist) for dist in distribution]
        self.results = [[] for _ in range(arms)]
    

    def generate_params(self, dist):
        if dist in ["normal", "uniform", "beta"]:
            return (np.random.uniform(0,10), np.random.uniform(0,10))
        else:
            return np.random.randint(0,10)
        
    def generate_reward(self, arm):
        dist = self.dist[arm]
        param = self.params[arm]
        match dist:
            case "normal":
                self.results[arm] += [np.random.normal(*param)]
            case "beta":
                self.results[arm] += [np.random.beta(*param)]
            case "uniform":
                self.results[arm] += [np.random.uniform(*param)]
            case _:
                print("There is an issue here. No cases match the dist.")

    def reset(self):
        self.params = [self.generate_params(dist) for dist in self.dist]
        self.results = [[] for _ in range(self.arms)]

    def generate_average(self):
        print(x for x in self.results)
        return [statistics.mean(x) if x else [0] for x in self.results]


@app.route('/')
def index():
    # To generate the scatterplot:
    img = io.BytesIO()
    plt.figure(figsize=(20, 7))
    
    for i, rewards in enumerate(bandit.results):
        x_values = [i] *len(rewards)
        plt.scatter(x_values, rewards, label=f'Arm {i+1}')
        print(i, rewards)

    plt.xlabel('Pulls')
    plt.ylabel('Reward')
    plt.title('Rewards Over Time for Each Arm')
    plt.legend()

    plt.xticks(ticks=range(bandit.arms), labels=range(1, bandit.arms + 1))

    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()

    return render_template('index.html', arms=range(bandit.arms), 
                           params=bandit.params, rewards = bandit.results, 
                           dist = bandit.dist, plot_url = plot_url, average = bandit.generate_average())

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