import React from 'react';
import PropsTypes from 'prop-types';
import {connect} from 'react-redux';
import SignupForm from '../forms/SignupForm';
import { signup } from '../../actions/users';

class SignupPage extends React.Component {
    submit = data => this.props.signup(data).then(() => this.props.history.push('/dashboard'));

    render() {
        return (
            <div>
                <SignupForm submit={this.submit}/>
            </div>
        );
    }
}

SignupPage.propTypes = {
    signup: PropsTypes.func.isRequired,
    history: PropsTypes.shape({
        push: PropsTypes.func.isRequired
    }).isRequired
};

export default connect(null, { signup })(SignupPage);