import React, {Component} from 'react';
import PropTypes from 'prop-types';
import CircularProgress from 'material-ui/CircularProgress';
import FriendComponent from './friend';

const FRIENDS = [
    {id: 1, username: 'AAAA', first_name: 'FN', last_name: 'LN', avatar: '/'},
    {id: 2, username: 'AAAA', first_name: 'FN', last_name: 'LN', avatar: '/'},
    {id: 3, username: 'AAAA', first_name: 'FN', last_name: 'LN', avatar: '/'},
];

export default class FriendshipRequestsComponent extends Component {

    state = {
        friendshipRequestsList: [],
        isLoading: true,
    };

    componentDidMount() {
        const requests = FRIENDS.map(
            request => <FriendComponent
                bsStyle="info"
                key={request.id}
                username={request.username}
                first_name={request.first_name}
                last_name={request.last_name}
            />,
        );
        this.setState({
            friendshipRequestsList: requests,
            isLoading: false,
        });
    }

    render() {
        return (
            <div> {this.state.isLoading ?
                <CircularProgress size={60} thickness={7}/> : this.state.friendshipRequestsList
            }
            </div>
        );
    }
}

FriendshipRequestsComponent.defaultProps = {
    isLoading: true,
};

FriendshipRequestsComponent.propTypes = {
    friendshipRequestsList: PropTypes.arrayOf.isRequired(PropTypes.element),
    isLoading: PropTypes.bool,
};
