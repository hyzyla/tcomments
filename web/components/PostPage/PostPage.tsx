import React, { FC } from 'react';
import css from './PostPage.module.css';
import { PostCard } from "../PostCard/PostCard";
import { Post, Comment } from "../../types";
import {Comments} from "../CommentsList/Comments";

export const postContext = React.createContext<Post | null>(null);

interface Props {
    post: Post;
    comments: Comment[],
}

export const PostPage: FC<Props> = (props) => {
    const { Provider } = postContext;
    return (
        <div className={css.root}>
            <div className={css.article}>
                <PostCard post={props.post}/>
                <Provider value={props.post}>
                    <Comments comments={props.comments}/>
                </Provider>
            </div>
        </div>
    );
};
