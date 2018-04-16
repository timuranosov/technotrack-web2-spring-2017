import React, {Component} from 'react';
import {Button, ButtonToolbar, ListGroupItem, Media} from 'react-bootstrap';
import PropTypes from 'prop-types';

export default class FriendComponent extends Component {
    render() {
        return (
            <ListGroupItem bsStyle={this.props.bsStyle}>
                <Media>
                    <Media.Body>
                        <Media.Heading>Username</Media.Heading>
                        <p>First name Last name</p>
                        <ButtonToolbar>
                            <Button bsStyle="primary">Написать</Button>
                            <Button bsStyle="link">Удалить из друзей</Button>
                        </ButtonToolbar>
                    </Media.Body>
                </Media>
            </ListGroupItem>
        );
    }
}

FriendComponent.propTypes = {
    bsStyle: PropTypes.string.isRequired,
};