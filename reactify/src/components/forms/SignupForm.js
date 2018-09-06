import React from 'react';
import {Form, Button, Message} from 'semantic-ui-react';
import isEmail from 'validator/lib/isEmail';
import InlineError from '../messages/InlineError';
import PropTypes from 'prop-types';
import parseErrors from '../utils/parseErrors';
import _ from 'lodash';

class SignupForm extends React.Component {
    state = {
        data: {
            email: '',
            // email2: '',
            password: '',
        },
        loading: false,
        errors: {}
    };

    onSubmit = (e) => {
        e.preventDefault();
        const errors = this.validate(this.state.data);
        this.setState({errors});
        if (Object.keys(errors).length === 0) {
            this.setState({loading: true});
            this.props
                .submit(this.state.data)
                .catch(err => this.setState({errors: {global: parseErrors(err.response.data)} , loading: false}))
        }
    };

    validate = data => {
        const errors = {};
        if (!isEmail(data.email)) errors.email = 'Invalid email';
        // if (!isEmail(data.email2)) errors.email2 = 'Invalid email';
        if (!data.password) errors.password = "Can't be blanc";

        return errors;
    };

    onChange = e =>
        this.setState({
            data: {...this.state.data, [e.target.name]: e.target.value}
        });

    render() {
        const {data, loading, errors} = this.state;

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
                {/*<Form.Field error={!!errors.email2}>*/}
                    {/*<label htmlFor="email2">Email confirmation</label>*/}
                    {/*<input*/}
                        {/*type="email"*/}
                        {/*id="email2"*/}
                        {/*name="email2"*/}
                        {/*placeholder="Repeat email"*/}
                        {/*value={data.email2}*/}
                        {/*onChange={this.onChange}/>*/}
                    {/*{errors.email2 && <InlineError text={errors.email2}/>}*/}
                {/*</ Form.Field>*/}
                <Form.Field error={!!errors.password}>
                    <label htmlFor="password">Password</label>
                    <input
                        type="password"
                        id="password"
                        name="password"
                        value={data.password}
                        placeholder="Make it secure"
                        onChange={this.onChange}/>
                    {errors.password && <InlineError text={errors.password}/>}

                </ Form.Field>

                <Button primary>Sign Up</Button>
            </Form>
        );
    }
}

SignupForm.propTypes = {
    submit: PropTypes.func.isRequired
};

export default SignupForm;