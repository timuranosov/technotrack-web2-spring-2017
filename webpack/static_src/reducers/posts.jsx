import React from 'react';
import update from 'react-addons-update';
import PostComponent from '../components/post';

import {LOAD_POSTS, LOAD_POSTS_FAIL, LOAD_POSTS_SUCCESS, SHOW_MODAL} from '../actions/posts';

const initialState = {
    posts: {},
    postIds: [],
    isLoading: false,
    postList: [],
};

export default function posts(store = initialState, action) {
    switch (action.type) {
        case LOAD_POSTS:
            return update(store, {isLoading: {$set: true}});
        case LOAD_POSTS_SUCCESS:
            const x = update(store, {
                posts: {
                    $merge: action.posts,
                },
                postIds: {
                    $merge: action.postIds,
                },
            });

            const list = action.postIds.map(post => <PostComponent key={post} id={post}/>);

            return update(x, {
                isLoading: {$set: false},
                postList: {
                    $set: list,
                },
            });

        case LOAD_POSTS_FAIL:
            return update(store, {isLoading: {$set: false}});

        case SHOW_MODAL:
            return update(store, {
                posts: {
                    [action.id]: {
                        modal: {
                            $set: action.option,
                        },
                    },
                },
            });


        default:
            return store;
    }
}