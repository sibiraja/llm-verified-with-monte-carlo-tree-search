### My Ideas

1. Increasing steerability with user and verifier feedback
    * User feedbacK: this could draw inspiration from the 3rd point below, but it would be interesting for a user to give a proof sketch at the beginning of the search and suggest proof techniques/tactics during the middle of the search or tweak/start over on the original proof sketch plan


2. Tree of Thoughts supports MCTS as one of its Search algorithms --> is there possbility for us to integrate Prof. Amin's MCTS into Tree of Thoughts? This might help with reasoning capabilities while also using the MCTS strategy

3.  On the note of creating a plan or proof sketch before proving, what if create a list of proof techniques/tactics and whenever we try to find the next best child, we could add a scoring mechanism that evaluates if a given child is likely to help in further advancing the proof state based on the original plan we devised -- this would entail keeping track of more information regarding the proof state in a node such as what tactic/technique it is
    * Bayesian framework could be applied here