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

const FieldName = styled.label`
    margin-left: 0.5em;
    margin-right: 0.5em;
`;

function FieldInput (props) {
    const { type, id, value, onChangeHandler, fieldname } = props;

    return (
        <>
            <FieldName 
                htmlFor={type === 'password' ? type : id } 
                value={value} 
                onChange={(e) => onChangeHandler(e.target.value)}
            >{ fieldname }
            </FieldName>
            <Input 
                id={type === 'password' ? type : id } 
                type={type} 
                value={value} 
                onChange={(e) => onChangeHandler(e.target.value)}/>
        </>
        
    );
}
  
export default FieldInput