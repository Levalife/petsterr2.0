import React, {Component} from 'react';
import {Form, Button, Message} from 'semantic-ui-react';
import Validator from 'validator';
import InlineError from '../messages/InlineError';
import PropTypes from 'prop-types';

class LoginForm extends Component {
    state = {
        data: {
            username: "",
            password: ""
        },
        loading: false,
        errors: {}
    };

    onChange = e =>
        this.setState({
            data: {...this.state.data, [e.target.name]: e.target.value}
        });


    onSubmit = () => {

        const errors = this.validate(this.state.data);
        this.setState({errors});
        if (Object.keys(errors).length === 0) {
            this.setState({loading: true});

            this.props
                .submit(this.state.data)
                .catch(err => this.setState({errors: {global: err.response.data.non_field_errors}, loading: false}));
        }
    };

    validate = (data) => {
        const errors = {};
        if (!data.username) errors.username = "Can't be blank";
        if (!Validator.isEmail(data.username)) errors.username = "Invalid email";
        if (!data.password) errors.password = "Can't be blank";
        return errors
    };

    render() {
        const {data, errors, loading} = this.state;
        return (
            <Form onSubmit={this.onSubmit} loading={loading}>
                {errors.global && (<Message negative>
                    <Message.Header>Something went wrong</Message.Header>
                    {errors.global.map(function (text, index) {
                    return <p>{text}</p>;
                })}
                </Message>)}
                <Form.Field error={!!errors.username}>
                    <label htmlFor="username">Email</label>
                    <input
                        type="text"
                        id="username"
                        name="username"
                        placeholder="example@example.com"
                        value={data.username}
                        onChange={this.onChange}/>
                    {errors.username && <InlineError text={errors.username}/>}
                </ Form.Field>
                <Form.Field error={!!errors.password}>
                    <label htmlFor="password">Password</label>
                    <input
                        type="text"
                        id="password"
                        name="password"
                        value={data.password}
                        placeholder="Make it secure"
                        onChange={this.onChange}/>
                    {errors.password && <InlineError text={errors.password}/>}

                </ Form.Field>
                <Button primary>Login</Button>
            </Form>

        );
    }
}

LoginForm.propTypes = {
    submit: PropTypes.func.isRequired,
};


export default LoginForm;
