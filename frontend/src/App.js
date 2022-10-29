
import './App.css';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import Profile from './pages/Profile.js'
import Commentary from './pages/Commentary.js'
import Rewards from './pages/Rewards.js'
import Home from './pages/Home';

function App() {
  return (
  <>
    <Router>
        {/* <NavBar /> */}
        <Route
          render={({ location }) => (
            // <AnimatePresence exitBeforeEnter>
              <Switch>
                <Route path="/" exact component={Home} />
                {/* <Route path="/video" exact component={Video} /> */}

                <Route path="/profile" exact component={Profile} />
                <Route path="/commentary" exact component={Commentary} />
                <Route path="/rewards" exact component={Rewards} />
                {/* <Route path="/random" exact component={Random} /> */}
              </Switch>
            // </AnimatePresence>
          )}
        />
      </Router>
  </>
  );
}

export default App;
