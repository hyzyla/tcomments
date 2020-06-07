import React, { FC } from 'react';
import css from './PostPage.module.css';
import { PostCard } from "../PostCard/PostCard";
import { CommentsList } from "../CommentsList/CommentsList";
import { Post, Comment } from "../../types";



interface Props {
    post: Post;
    comments: Comment[]
}


export const PostPage: FC<Props> = ({ post, comments }) => {
    return (
        <div className={css.root}>
            <div className={css.article}>
                <PostCard post={post}/>
                <CommentsList comments={comments}/>
            </div>
        </div>
    );
};
