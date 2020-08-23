import React, { FC } from 'react';

import { Post } from '../../types';

import {PostText} from "./PostText";

import css from './PostCard.module.css';

interface Props {
    post: Post;
}

export const PostCard: FC<Props> = ({ post }) => {
    return (
        <div className={css.card}>
            <PostText html={post.textHTML} />
        </div>
    )
};
