import React, { Component } from 'react';
import CircularProgress from 'material-ui/CircularProgress';
import PostComponent from './post';


class PostListComponent extends Component {
  render() {
    const list = this.props.postList.map(
      (post, i) => <PostComponent
        key={i}
        author={post.author}
        content={post.content}
        date={post.date}
      />,
    );
    return (
      <div>{ this.props.isLoading ?
        <CircularProgress size={60} thickness={5} /> : list
      }
      </div>
    );
  }
}
PostListComponent.defaultProps = {
  isLoading: true,
};

PostListComponent.propTypes = {
  postList: React.PropTypes.arrayOf(React.PropTypes.shape({
    author: React.PropTypes.shape({
      username: React.PropTypes.string,
      avatarUrl: React.PropTypes.string,
    }).isRequired,
    date: React.PropTypes.string.isRequired,
    content: React.PropTypes.string.isRequired,
  })).isRequired,
  isLoading: React.PropTypes.bool,
};

export default PostListComponent;
