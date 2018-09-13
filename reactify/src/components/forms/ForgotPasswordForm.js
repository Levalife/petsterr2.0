import React, {Component} from 'react';
import {Form, Button, Message} from 'semantic-ui-react';
import Validator from 'validator';
import InlineError from '../messages/InlineError';
import PropTypes from 'prop-types';
import _ from "lodash";

class ForgotPasswordForm extends Component {
    state = {
        data: {
            email: "",
        },
        loading: false,
        errors: {}
    };

    onChange = e =>
        this.setState({
            data: {...this.state.data, [e.target.name]: e.target.value}
        });


    onSubmit = (e) => {
        e.preventDefault();
        const errors = this.validate(this.state.data);
        this.setState({errors});
        if (Object.keys(errors).length === 0) {
            this.setState({loading: true});

            this.props
                .submit(this.state.data)
                .catch(err => this.setState({errors: {global: err.response.data}, loading: false}));
        }
    };

    validate = (data) => {
        const errors = {};
        if (!data.email) errors.email = "Can't be blank";
        if (!Validator.isEmail(data.email)) errors.email = "Invalid email";
        return errors
    };

    render() {
        const {data, errors, loading} = this.state;
        return (
            <Form onSubmit={this.onSubmit} loading={loading}>
                {errors.global && (<Message negative>
                    <Message.Header>Something went wrong</Message.Header>
                    {_.forEach(errors.global, (val, index) => {
                        return <p>{val}</p>
                    })}
                </Message>)}
                <Form.Field error={!!errors.email}>
                    <label htmlFor="email">Email</label>
                    <input
                        type="email"
                        id="email"
                        name="email"
                        placeholder="example@example.com"
                        value={data.email}
                        onChange={this.onChange}/>
                    {errors.email && <InlineError text={errors.email}/>}
                </ Form.Field>
                <Button primary>Send email</Button>
            </Form>

        );
    }
}

ForgotPasswordForm.propTypes = {
    submit: PropTypes.func.isRequired,
};


export default ForgotPasswordForm;
