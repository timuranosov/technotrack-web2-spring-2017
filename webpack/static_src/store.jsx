import {applyMiddleware, createStore} from 'redux';
import {composeWithDevTools} from 'redux-devtools-extension';
import createHistory from 'history/createBrowserHistory';
import {routerMiddleware} from 'react-router-redux';
import thunk from 'redux-thunk';

import initReducers from './reducers/index';
import normalizeMiddleware from './middleware/normalize';

export const history = createHistory();
const routingMiddleware = routerMiddleware(history);

export default function initStore() {
    const initialStore = {};
    return createStore(initReducers, initialStore,
        composeWithDevTools(applyMiddleware(
            routingMiddleware,
            normalizeMiddleware,
            thunk,
        )));
}
