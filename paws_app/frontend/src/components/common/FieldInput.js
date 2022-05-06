import styled from 'styled-components';
import React, { Component, Fragment } from "react"

const Input = styled.input`
    padding: 0.5em;
    color: #458642;
    border-radius: 30px;
    border-color: #458642;
    border-style: solid;
    border-width: 2px;
    min-width: 300px;
    margin-bottom: 10px;
    height: 25px;
`;

const FieldName = styled.div`
    margin-left: 0.5em;
    margin-right: 0.5em;
`;

class FieldInput extends Component {
    render() {
        return (
            <>
                <FieldName>{ this.props.fieldname }</FieldName>
                <Input type="text" />
            </>
            
      )
    }
  }
  
export default FieldInput