import NewTemplate from "./components/NewTemplate";
import React from "react";
import ReactDOM from "react-dom";
import 'bootstrap/dist/css/bootstrap.css';

const NewResume = () => {
    return <NewTemplate />;
};

ReactDOM.render(<NewResume />, document.getElementById("root"));