import React, {Component} from 'react';
import {Link} from 'react-router-dom'
import cookie from "react-cookies";

class LoginForm extends Component {

    constructor(props) {
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleInputChange = this.handleInputChange.bind(this);
        this.state = {
            token: null,
        }
    }

    loginJWTToken(data) {
        const endpoint = '/api-token-auth/';
        const csrfToken = cookie.load('csrftoken');
        let thisComp = this;

        if (csrfToken !== undefined) {
            let lookupOptions = {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken  // field name from Django docs
                },
                body: JSON.stringify(data),
            };

            fetch(endpoint, lookupOptions)
                .then(function (response) {
                    return response.json()
                }).then(function (responseData) {
                console.log(responseData);
                thisComp.token = responseData.token;
                localStorage.setItem('jwtToken', responseData.token);
                // sessionStorage.setItem('jwtToken', responseData.token);
                thisComp.clearForm();

            }).catch(function (error) {
                console.log("error", error);
                alert(error)
            })
        }
    }

    loginUser(data) {
        const endpoint = '/api/v1/users/login/';
        const csrfToken = cookie.load('csrftoken');
        let thisComp = this;

        if (csrfToken !== undefined) {
            let lookupOptions = {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken  // field name from Django docs
                },
                body: JSON.stringify(data),
            };

            fetch(endpoint, lookupOptions)
                .then(function (response) {
                    return response.json()
                }).then(function (responseData) {
                console.log(responseData);
                if (responseData.token) {
                    thisComp.token = responseData.token;
                    localStorage.setItem('Token', responseData.token);
                    // sessionStorage.setItem('Token', responseData.token);
                    thisComp.clearForm();
                } else {
                    alert(responseData.non_field_errors)
                }

            }).catch(function (error) {
                console.log("error", error);
                alert(error)
            })
        }
    }

    defaultState() {
        this.setState({
            username: '',
            password: ''
        })
    }

    clearForm() {
        this.loginUserForm.reset();
        this.defaultState();
    }

    handleSubmit(event) {
        event.preventDefault();
        let data = this.state;
        this.loginUser(data)
    }

    handleInputChange(event) {
        event.preventDefault();
        let key = event.target.name;
        let value = event.target.value;
        if (key === 'title') {
            if (value.length > 50) {
                alert('This title is too long!')
            }
        }
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    render() {
        return (
            <div>
                <form onSubmit={this.handleSubmit} ref={(el) => this.loginUserForm = el}>
                    <div className='form-group'>
                        <input type='text'
                               id='username'
                               name='username'
                               className="form-control"
                               placeholder="Email address"
                               onChange={this.handleInputChange}
                               required='required'/>
                    </div>
                    <div className='form-group'>
                        <input type='password'
                               id='password'
                               name='password'
                               className="form-control"
                               placeholder="Password"
                               onChange={this.handleInputChange}
                               required='required'/>
                    </div>
                    <button>Login</button>
                </form>
            </div>
        );
    }
}

export default LoginForm;
