/* global document: true */
/* global window: true */
import React, {Component} from 'react';
import {Col, Grid} from 'react-bootstrap';
import PropTypes from 'prop-types';
import '../styles/bootstrap-3/css/bootstrap.css';
import NavBarTop from './navBarTop';
import NavBarLeft from './navBarLeft';
import PostListLayoutComponent from './postListLayout';
import FriendListLayout from './friendList';
import UserPage from './userPage';
import ChatsListComponent from './chatsList';

class LayoutComponent extends Component {
    state = {
        user: {
            pk: 0,
            username: '',
            first_name: '',
            last_name: '',
            avatar: null,
        },
        currentPageName: 'news',
    };

    componentDidMount() {
        fetch('http://localhost:8000/api/users/?format=json',
            {
                method: 'GET',
                credentials: 'same-origin',
            })
            .then(promise => promise.json())
            .then((json) => {
                this.setState({
                    user: json[0],
                });
            });
    }

    onCreate = (post) => {
        this.setState({
            postList: [post, ...this.state.postList],
        });
    };

    onMenuSelect = (currentMenu) => {
        this.setState({
            currentPageName: currentMenu,
        });
    };

    render() {
        let page = null;
        switch (this.state.currentPageName) {
            case 'news':
                page = <PostListLayoutComponent/>;
                break;
            case 'mypage':
                page = <UserPage user={this.state.user}/>;
                break;
            case 'friends':
                page = <FriendListLayout/>;
                break;
            case 'chats':
                page = <ChatsListComponent/>;
                break;
            default:
                page = <PostListLayoutComponent/>;
        }

        return (
            <div>
                <NavBarTop user={this.state.user}/>
                <Grid fluid>
                    <NavBarLeft onSelect={this.onMenuSelect}/>
                    <Col xs={12} md={8}>
                        {page}
                    </Col>
                </Grid>
            </div>
        );
    }
}

LayoutComponent.propTypes = {
    onSelect: PropTypes.func.isRequired,
};

export default LayoutComponent;