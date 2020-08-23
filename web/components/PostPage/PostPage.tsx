import React, { FC } from 'react';
import css from './PostPage.module.css';
import { PostCard } from "../PostCard/PostCard";
import {Post, Comment, User} from "../../types";
import {Comments} from "../CommentsList/Comments";

export const postContext = React.createContext<Post | undefined>(undefined);
export const currentUserContext = React.createContext<User | undefined>(undefined);

interface Props {
    post: Post;
    comments: Comment[],
    currentUser?: User,
}

export const PostPage: FC<Props> = (props) => {
    const { Provider: PostContextProvider } = postContext;
    const { Provider: CurrentUserContextProvider } = currentUserContext;
    return (
        <div className={css.root}>
            <div className={css.article}>
                <PostCard post={props.post}/>
                <PostContextProvider value={props.post}>
                    <CurrentUserContextProvider value={props.currentUser}>
                        <Comments comments={props.comments}/>
                    </CurrentUserContextProvider>
                </PostContextProvider>
            </div>
        </div>
    );
};
