import React, {Component} from 'react';
import {ListGroup} from 'react-bootstrap';
import FriendsComponent from './friends';
import {FRIENDSHIP_REQUESTS, FRIENDSHIP_WAITINGS, FRIENDSHIPS} from './friend';

export default class FriendListLayout extends Component {
    render() {
        return (
            <ListGroup>
                <FriendsComponent type={FRIENDSHIP_REQUESTS}/>
                <FriendsComponent type={FRIENDSHIP_WAITINGS}/>
                <FriendsComponent type={FRIENDSHIPS}/>
            </ListGroup>
        );
    }
}
