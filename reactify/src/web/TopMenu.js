import React, {Component} from 'react';
import { Link } from 'react-router-dom'

class TopMenu extends Component {
    render() {
        return (
            <div className="main-menu-block">
                <div className="logo"><a href="/">PetsTerr</a></div>
                <ul>
                    <li><Link maintainScrollPosition={false} to={{
                        pathname: '/kennels',
                        state: {fromDashboard: false}
                    }}>Kennels and catteries</Link></li>
                    {}
                    {/*<li><a href="{% url 'users:profile_page' %}">Profile</a></li>*/}
                    {/*<li><a href="{% url 'users:logout_page' %}">Log Out</a></li>*/}
                    {/*<li><a href="{% url 'users:login_page' %}">Log In</a></li>*/}
                    {/*<li><a href="{% url 'users:signup_page' %}">Sign Up</a></li>*/}
                </ul>
            </div>
        );
    }
}

export default TopMenu;
