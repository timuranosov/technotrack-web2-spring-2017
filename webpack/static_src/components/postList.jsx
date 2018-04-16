import React, {Component} from 'react';
import CircularProgress from 'material-ui/CircularProgress';
import PostComponent from './post';
import PropTypes from 'prop-types';


class PostListComponent extends Component {
    render() {
        // if (this.props.postList.length === 0) {
        //   return null;
        // }

        const list = this.props.postList.map(
            post => <PostComponent
                key={post.id}
                author={post.author}
                title={post.title}
                content={post.content}
                date={post.created}
            />,
        );
        return (
            <div>{this.props.isLoading ?
                <CircularProgress size={60} thickness={7}/> : list
            }
            </div>
        );
    }
}

PostListComponent.defaultProps = {
    isLoading: true,
};

PostListComponent.propTypes = {
    postList: PropTypes.arrayOf.isRequired(PropTypes.shape({
        author: PropTypes.shape.isRequired({
            username: PropTypes.string,
            avatarUrl: PropTypes.string,
        }).isRequired,
        date: PropTypes.string.isRequired,
        content: PropTypes.string.isRequired,
    })).isRequired,
    isLoading: PropTypes.bool,
};

export default PostListComponent;