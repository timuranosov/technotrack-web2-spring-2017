/* global document: true */
/* global window: true */
import React, { Component } from 'react';
import { Grid, Col } from 'react-bootstrap';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import '../styles/bootstrap-3/css/bootstrap.css';
import NavbarTop from './navBarTop';
import NavbarLeft from './navBarLeft';
import PostListLayoutComponent from './postListLayout';
import FriendListLayout from './friendList';
import UserPage from './userPage';
import ChatsListComponent from './chatsList';
import PeopleSearchComponent from './peopleSearch';
import { fetchProfile } from '../actions/account';

class LayoutComponent extends Component {
  componentDidMount() {
    this.props.fetchProfile();
    console.log(this.props);
  }

  onCreate = (post) => {
    this.setState({
      postList: [post, ...this.state.postList],
    });
  };

  render() {
    console.log(this.props.children);
    let page = null;
    switch (this.props.currentPage) {
      case 'news': page = <PostListLayoutComponent />;
        break;
      case 'mypage': page = <UserPage id={this.props.profile.id} />;
        break;
      case 'friends': page = <FriendListLayout />;
        break;
      case 'chats': page = <ChatsListComponent />;
        break;
      case 'people': page = <PeopleSearchComponent />;
        break;
      default:
        page = <PostListLayoutComponent />;
    }

    return (
      <div>
        <NavbarTop user={this.props.profile} />
        <Grid fluid>
          <NavbarLeft onSelect={this.onMenuSelect} />
          <Col xs={12} md={8}>
            { page }
          </Col>
        </Grid>
      </div>
    );
  }
}

// LayoutComponent.propTypes = {
//   onSelect: PropTypes.func.isRequired,
// };

const mapStateToProps = state => ({
  currentPage: state.router.currentPage,
  profile: state.layout.account,
});

const mapDispatchToProps = distpatch => ({
  ...bindActionCreators({
    fetchProfile,
  }, distpatch),
});

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(LayoutComponent);
