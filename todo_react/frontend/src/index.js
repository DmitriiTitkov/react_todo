import React from "react";
import ReactDOM from "react-dom";


class App extends React.Component {
    render(){
        return (
            <div>
                Hello everybody!
            </div>
        )
    }
}

ReactDOM.render(<App/>, document.getElementById("spa-root"));