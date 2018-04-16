import React, {Component} from 'react';
import {Button, Modal} from 'react-bootstrap';
import PropTypes from 'prop-types';
import Avatar from 'material-ui/Avatar';

export default class ModalComponent extends Component {
    close = () => {
        this.props.onClickShow(false);
    };

    render() {
        return (
            <div>
                <Modal show={this.props.showModal} onHide={this.close}>
                    <Modal.Header closeButton>
                        <Modal.Title>
                            <Avatar src={this.props.user.avatar} size={50}/>
                            {this.props.user.username}
                        </Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        {this.props.content}
                    </Modal.Body>
                    <Modal.Footer>
                        {this.props.date}
                        {<Button onClick={this.close}>X</Button>}
                    </Modal.Footer>
                </Modal>
            </div>
        );
    }
}

ModalComponent.propTypes = {
    user: PropTypes.shape({
        pk: PropTypes.number,
        username: PropTypes.string,
        avatar: PropTypes.string,
    }),
    date: PropTypes.string.isRequired,
    content: PropTypes.string.isRequired,
    showModal: PropTypes.bool.isRequired,
    onClickShow: PropTypes.func.isRequired,
};
