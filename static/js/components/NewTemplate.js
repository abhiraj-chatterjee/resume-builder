import React from "react";
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
// import logo_image from "../../img/react.png";
import "../../css/NewTemplateStyle.css";

function SomeComponent () {
    return (
        <Container>
            <h3>Choose a template:</h3>
            <br />
            <Button href="/new/resume/technical" variant="outline-danger" size="lg">Technical Resume</Button>
        </Container>
    );
}

export default SomeComponent;