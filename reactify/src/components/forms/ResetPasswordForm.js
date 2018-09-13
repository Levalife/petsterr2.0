import React, {Component} from 'react';
import {Form, Button, Message} from 'semantic-ui-react';
import InlineError from '../messages/InlineError';
import PropTypes from 'prop-types';
import _ from "lodash";

class ResetPasswordForm extends Component {
    state = {
        data: {
            token: this.props.token,
            new_password: "",
            confirm_password: "",
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
        if (!data.new_password) errors.new_password = "Can't be blank";
        if (data.new_password != data.confirm_password) errors.new_password = "Passwords must match";
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
                <Form.Field error={!!errors.new_password}>
                    <label htmlFor="password">New password</label>
                    <input
                        type="password"
                        id="new_password"
                        name="new_password"
                        placeholder="Make it secure"
                        value={data.new_password}
                        onChange={this.onChange}/>
                    {errors.new_password && <InlineError text={errors.new_password}/>}
                </ Form.Field>
                <Form.Field error={!!errors.confirm_password}>
                    <label htmlFor="password">Confirm new password</label>
                    <input
                        type="password"
                        id="confirm_password"
                        name="confirm_password"
                        placeholder="Repeat new password"
                        value={data.confirm_password}
                        onChange={this.onChange}/>
                    {errors.confirm_password && <InlineError text={errors.confirm_password}/>}
                </ Form.Field>
                <Button primary>Save</Button>
            </Form>

        );
    }
}

ResetPasswordForm.propTypes = {
    submit: PropTypes.func.isRequired,
    token: PropTypes.string.isRequired,
};


export default ResetPasswordForm;
