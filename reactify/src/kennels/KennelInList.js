import React, {Component} from 'react';
import { Link } from 'react-router-dom'

class KennelInList extends Component {
    render() {
        const {kennel} = this.props;
        const {elClass} = this.props;
        const showContent = elClass === 'card' ? 'd-block' : 'd-none';
        return (
            <div>
                {kennel !== undefined ? <div className={elClass}>

                    <h1><Link maintainScrollPosition={false} to={{
                        pathname: `/kennels/${kennel.slug}`,
                        state: {fromDashboard: false}
                    }}>{kennel.title}</Link></h1>
                    <p className={showContent}>{kennel.type}</p>
                </div> : ''
                }
            </div>
        );
    }
}

export default KennelInList;
